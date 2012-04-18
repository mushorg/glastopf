# Copyright (C) 2011  Lukas Rist
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sandbox.apd_sandbox as sandbox

import modules.handlers.emulators.unknown as unknown_emulator
import modules.handlers.emulators.rfi as rfi_emulator
import modules.handlers.emulators.lfi as lfi_emulator
import modules.handlers.emulators.sqli as sqli_emulator
import modules.handlers.emulators.phpmyadmin as pma_emulator
import modules.handlers.emulators.file_server as fs_emulator


def unknown(attack_event):
    emulator = unknown_emulator.DorkList()
    attack_event.response += emulator.get_response()
    return attack_event


def style_css(attack_event):
    with open('modules/handlers/emulators/style/style.css', 'r') as style_file:
        attack_event.response = style_file.read()
    return attack_event


def robots_txt(attack_event):
    with open('modules/handlers/emulators/robots/robots.txt', 'r') as robot_file:
        attack_event.response = robot_file.read()
    return attack_event


def rfi(attack_event):
    emulator = rfi_emulator.RFIEmulator()
    attack_event.file_name = emulator.download_file(attack_event.parsed_request.url)
    if attack_event.file_name:
        attack_event.response += sandbox.run(attack_event.file_name)
    return attack_event


def lfil(attack_event):
    emulator = lfi_emulator.LFIEmulator()
    file_contents = emulator.getContents(attack_event.parsed_request.url)
    attack_event.response += file_contents
    return attack_event


def lfiw(attack_event):
    # TODO: Implement Windows local file incusion handler  
    attack_event.response += "lfi-windows handled"
    return attack_event


def sql(attack_event):
    emulator = sqli_emulator.SQLiEmulator()
    emulator.handle(attack_event)
    return attack_event


def phpmyadmin(attack_event):
    emulator = pma_emulator.PMAEmulator()
    emulator.handle(attack_event)
    return attack_event


def file_server(attack_event):
    emulator = fs_emulator.FileServer()
    emulator.handle(attack_event)
    return attack_event
