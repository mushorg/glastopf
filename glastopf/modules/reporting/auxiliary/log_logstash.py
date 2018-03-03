import logging
import os
import logstash

logger = logging.getLogger(__name__)


# Global logger for logstash provides an interface for different brokers

from glastopf.modules.reporting.auxiliary.base_logger import BaseLogger


class LogLogStash(BaseLogger):
    def __init__(self, data_dir, work_dir, config="glastopf.cfg"):
        config = os.path.join(work_dir, config)
        BaseLogger.__init__(self, config)

        if self.config.getboolean("logstash", "enabled"):
            self.host = self.config.get("logstash", "host")
            self.port = int(self.config.getint("logstash", "port"))
            self.options = {
                "enabled": self.config.getboolean("logstash", "enabled"),
            }

            self.handler = self.config.get("logstash", "handler")

            if self.handler == "AMQP":
                self.username = self.config.get("logstash", "username")
                self.password = self.config.get("logstash", "password")
                self.exchange = self.config.get("logstash", "exchange")
                self.durable = self.config.getboolean("logstash", "durable")
            elif self.handler != "TCP" and self.handler != "UDP":
                raise Exception("Incorrect logstash handler defined, please use AMQP, UDP or TCP")
            self._setup_handler()
        else:
            self.options = {"enabled": False}

    def _setup_handler(self):
        logstash_handler = None

        if self.handler == 'AMQP':
            logstash_handler = logstash.AMQPLogstashHandler(version=1,
                                                            host=self.host,
                                                            durable=self.durable,
                                                            username=self.username,
                                                            password=self.password,
                                                            exchange=self.exchange)
        elif self.handler == 'TCP':
            logstash_handler = logstash.TCPLogstashHandler(self.host, self.port, version=1)
        elif self.handler == "UDP":
            logstash_handler = logstash.UDPLogstashHandler(self.host, self.port, version=1)

        self.attack_logger = logging.getLogger('python-logstash-handler')
        self.attack_logger.setLevel(logging.INFO)
        self.attack_logger.addHandler(logstash_handler)

    def insert(self, attack_event):
        message = "Glaspot: %(pattern)s attack method from %(source)s against %(host)s:%(port)s." \
                  "[%(method)s %(url)s]" % {
                      'pattern': attack_event.matched_pattern,
                      'source': ':'.join((attack_event.source_addr[0], str(attack_event.source_addr[1]))),
                      'host': attack_event.sensor_addr[0],
                      'port': attack_event.sensor_addr[1],
                      'method': attack_event.http_request.request_verb,
                      'url': attack_event.http_request.request_url,
                  }

        extra = {
            "pattern":     attack_event.matched_pattern,
            "source_addr": attack_event.source_addr[0],
            "source_port": attack_event.source_addr[1],
            "sensor_addr": attack_event.sensor_addr[0],
            "sensor_port": attack_event.sensor_addr[1],
            "method":      attack_event.http_request.request_verb,
            "url":         attack_event.http_request.request_url,
        }

        self.attack_logger.info(message, extra = extra)


