# Git Processor

A git log processor for better stats.

## Setup

Using Docker:

```bash
# build the image:
docker build -t git-processor .
# Run image:
docker run -it seed-app
```

## Testing

To find out more info about the testing configuration, check out the `tox.ini` file.

```bash
# Run the test suite
tox
# Run the linter:
tox -e lint
```