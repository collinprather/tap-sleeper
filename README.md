# tap-sleeper ![logo](logo.gif)


[![Singer](https://img.shields.io/badge/Singer-Tap-purple.svg)](https://hub.meltano.com/taps/sleeper)
[![PyPI](https://img.shields.io/pypi/v/tap-sleeper.svg?color=blue)](https://pypi.org/project/tap-sleeper/)
[![Python versions](https://img.shields.io/pypi/pyversions/tap-sleeper.svg)](https://pypi.org/project/tap-sleeper/)
[![Super-Linter](https://github.com/collinprather/tap-sleeper/actions/workflows/super-linter.yml/badge.svg)](https://github.com/collinprather/tap-sleeper/actions/workflows/super-linter.yml)
[![TestPyPI](https://github.com/collinprather/tap-sleeper/actions/workflows/test-pypi.yml/badge.svg)](https://github.com/collinprather/tap-sleeper/actions/workflows/test-pypi.yml)
[![Test Tap](https://github.com/collinprather/tap-sleeper/actions/workflows/test-tap.yml/badge.svg)](https://github.com/collinprather/tap-sleeper/actions/workflows/test-tap.yml)
[![CodeQL](https://github.com/collinprather/tap-sleeper/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/collinprather/tap-sleeper/actions/workflows/codeql-analysis.yml)

`tap-sleeper` is a [Singer](https://hub.meltano.com/singer/spec) tap for the [Sleeper](https://sleeper.app/) [api](https://docs.sleeper.app/), built with the [Meltano Tap SDK](https://sdk.meltano.com), which makes it easy to pull the latest news about or status of any NFL players, or granular information about your fantasy football league.


## Installation

```bash
pipx install tap-sleeper
```

## Configuration

### Accepted Config Options

| **Property**                    | **Type** | **Required** | **Description**                                                                |
|---------------------------------|----------|--------------|--------------------------------------------------------------------------------|
| sport                           | string   | True         | Professional sport league, ie nfl, nba, etc                                    |
| league_id                       | string   | False        | Unique identifier for the sleeper league                                       |
| trending_players_lookback_hours | integer  | False        | Total hours to lookback when requesting the current trending players           |
| trending_players_limit          | integer  | False        | Total number of players to return when requesting the current trending players |

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-sleeper --about
```

## Usage

You can easily run `tap-sleeper` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-sleeper --version
tap-sleeper --help
tap-sleeper --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_sleeper/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-sleeper` CLI interface directly using `poetry run`:

```bash
poetry run tap-sleeper --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-sleeper
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-sleeper --version
# OR run a test `elt` pipeline:
meltano elt tap-sleeper target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
