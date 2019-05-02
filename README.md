![](https://img.shields.io/pypi/l/ccid.svg?style=flat) ![](https://img.shields.io/pypi/pyversions/ccid.svg?style=flat) ![](https://img.shields.io/pypi/v/ccid.svg) ![](https://img.shields.io/pypi/wheel/ccid.svg?style=flat)

# CCID library and tool

## Getting Started
We require Python >= 3.6 and corresponding `pip3` command.

We intend to support Linux, Windows and macOS. The requirement `pyusb` depends on `libusb`, which is likely pre-installed on Linux systems. On Windows, you may need to [install a driver](https://github.com/libusb/libusb/wiki/Windows#driver-installation).

To get started, run `pip3 install ccid`, this installs both the `ccid` library and the `ccid` command-line interface.

For development, we suggest you run `make init` instead, which

- sets up a virtual environment
- installs development requirements such as `black`
- installs `ccid` as symlink using our packaging tool `flit`, including all runtime dependencies listed in [`pyproject.toml`](pyproject.toml)

One way to ensure the virtual environment is active is to use [direnv](https://direnv.net/).

## CCID Tool
For help, run `ccid --help` after installation. The tool has a hierarchy of commands and subcommands.

Example:

```bash
ccid version  # outputs version of installed `ccid` library and tool
```

## Library Usage

Work in progress, example usage:

```python
import ccid

(...)
```

Comprehensive documentation coming, for now these are the main components

- `ccid.reader`: connect to and interface with CCID devices
- `ccid.cli`: implementation of the `ccid` command-line interface

## License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or
  http://www.apache.org/licenses/LICENSE-2.0)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

## Contributing
Any contribution intentionally submitted for inclusion in the work by you, as defined in the Apache-2.0 license, shall be dual licensed as above, without any additional terms or conditions.

Code is to be formatted and linted according to [Black](https://black.readthedocs.io/) and our [Flake8](http://flake8.pycqa.org/en/latest/) [configuration](.flake8)
Run `make check` to test compliance, run `make fix` to apply some automatic fixes.

We keep a [CHANGELOG](CHANGELOG.md).