# Journal CLI
A simple command line interface tool to manage my Journal entries quickly.
This project follows - _somewhat_ - the guidelines for journals mentioned by [Letícia Portella](leportella) on this [blog post](https://leportella.com/impostor-syndrome.html/).

## Instalation

**Manual**

```bash
$ git clone <this repo>
$ cd journal-cli
$ python3 setup.py install
```

## Usage

```bash
$ journal
```

### New

Creates root folder of your Journal and the **yaml** file containing configuration about the Journal.

```bash
$ journal new <folder-name>
```

Options:

  --no-conf Creates an empty configuration file

### Open

Opens, or create a new week entry, for the current year with your default editor.

```bash
$ journal open
```

[me]: https://github.com/amancioandre
[leportella]: https://github.com/leportella