#!/usr/bin/env python3
import os
import sys
import shutil
import time
import click
import json

try:
    from urllib.request import urlopen, Request
except:
    from urllib import urlopen
# pylint: disable=no-value-for-parameter
HEADER = '''
version: '3'
services:
'''

SERVICE = '''
  sslibev-{port}:
    container_name: sslibev-{port}-{method}
    image: shadowsocks/shadowsocks-libev:edge
    ports:
      - "{port}:{port}/tcp"
      - "{port}:{port}/udp"
    environment:
      - METHOD={method}
      - PASSWORD={password}
      - SERVER_PORT={port}
    restart: always
'''

OUTPUT = 'docker-compose.yml'


def show_servers(method, password, ports):
    server_ip = json.load(
        urlopen(Request("https://ip.cn", headers={'User-Agent': 'curl/7.54.0'})))['ip']
    # ss://method:password@server:port
    # ssr://server:port:protocol:method:obfs:password_base64/?suffix_base64
    click.echo('Server configurations: ')
    for pt in ports:
        click.echo('ss://{method}:{password}@{server}:{port}'.format(
            method=method, password=password, server=server_ip, port=pt))

def print_help():
    ctx = click.get_current_context()
    click.echo(ctx.get_help())
    ctx.exit()


@click.command()
@click.option('-', '--port', default=9001, show_default=True,
              prompt='Set start port of servers',
              help='Server start port.')
@click.option('-n', '--numbers', default=2, show_default=True,
              prompt='Set number of servers',
              help="Count of servers.")
@click.option('-m', '--method', default='chacha20-ietf-poly1305', show_default=True,
              prompt='Set encrypt method',
              help='Server encrypt method.')
@click.option('-s', '--password', default='shadowsocks',
              show_default=True,
              prompt='Set server password',
              confirmation_prompt=True,
              help='Server password.')
def generate(port, numbers, method, password):
    '''This script generate sslibev docker-compose.yml file fro you.'''
    ports = list(range(port, port+numbers))
    click.echo('Server ports: {}\nServer encrypt method: {}\nServer password: {}'.format(
        ports, method, password))
    if os.path.isfile(OUTPUT):
        #shutil.move(OUTPUT, '{}-{}'.format(int(time.time()), OUTPUT))
        shutil.move(OUTPUT, '{}.old'.format(OUTPUT))
    with open(OUTPUT, 'w') as f:
        f.write(HEADER)
        for pt in ports:
            f.write(SERVICE.format(port=pt, method=method, password=password))
    click.echo(
        'Congratulations! {} generated.\nNow you can start servers using `docker-compose up -d`.'.format(OUTPUT))
    # show_servers(method, password, ports)


if __name__ == "__main__":
    generate()
