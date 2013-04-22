#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


import smtplib
from email.mime.text import MIMEText

from ConfigParser import ConfigParser
from glastopf.modules.reporting.auxiliary.base_logger import BaseLogger


class LogMail(BaseLogger):
    def __init__(self, data_dir, config="glastopf.cfg"):
        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "enabled": conf_parser.getboolean("mail", "enabled"),
            "user": conf_parser.get("mail", "user"),
            "pwd": conf_parser.get("mail", "pwd"),
            "mail_from": conf_parser.get("mail", "mail_from"),
            "mail_to": conf_parser.get("mail", "mail_to"),
            "smtp_host": conf_parser.get("mail", "smtp_host"),
            "smtp_port": conf_parser.get("mail", "smtp_port"),
            "patterns": conf_parser.get("mail", "patterns"),
        }

    def _build_mail_body_event(self, attack_event):
        mail_msg = 'New attack from %s with request %s' % (attack_event.source_addr[0], attack_event.http_request.request_url)
        mail_msg += '\nComplete Request:\n\n'
        mail_msg += '%s %s' % (attack_event.http_request.request_verb, attack_event.http_request.request_url)
        for header in attack_event.http_request.request_header.keys():
            mail_msg += '\n%s: %s' % (header, attack_event.http_request.request_header[header])

        if attack_event.http_request.request_body:
            mail_msg += '\n\n%s' % attack_event.http_request.request_body

        msg = MIMEText(mail_msg)
        return msg

    def send_mail(self, attack_event):
        msg = self._build_mail_body_event(attack_event)
        msg['Subject'] = 'Honeypot Update'
        msg['From'] = self.options["mail_from"]
        msg['To'] = self.options["mail_to"]

        server = smtplib.SMTP('%s:%s' % (self.options["smtp_host"], self.options["smtp_port"]))
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.ehlo_or_helo_if_needed()
        server.login(self.options["user"], self.options["pwd"])
        server.sendmail(self.options["user"], self.options["mail_to"], msg.as_string())
        server.quit()

    def insert(self, attack_event):
        patterns = self.options["patterns"]

        # if the wildcard '*' is used, every new event will be notified by email
        if patterns == '*':
            self.send_mail(attack_event)
            return

        # otherwise an email notification will be sent
        # only if a specified matched pattern is identified
        if attack_event.matched_pattern in patterns.split(","):
            self.send_mail(attack_event)

