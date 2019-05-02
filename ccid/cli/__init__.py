# -*- coding: utf-8 -*-
#
# Copyright 2019 SoloKeys Developers
#
# Licensed under the Apache License, Version 2.0, <LICENSE-APACHE or
# http://apache.org/licenses/LICENSE-2.0> or the MIT license <LICENSE-MIT or
# http://opensource.org/licenses/MIT>, at your option. This file may not be
# copied, modified, or distributed except according to those terms.

import click

import ccid


@click.group()
def ccid_cli():
    pass


@click.command()
def version():
    """Version of ccid library and tool."""
    print(ccid.__version__)


ccid_cli.add_command(version)
