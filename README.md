# nbweb
`nbweb` is short for no bloat web

## description
`nbweb` is a simple tool to extract data from websites

## installation
```sh
pip install nbweb
```

## usage
```sh
nbweb <url>

# return output in text format
nbweb --format=txt <url>

# return rss feed
nbweb --rss <url>

# check if website is supported
nbweb --supported <url>

# check the version
nbweb -v
```

## about
inspired by [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## note
- this application is currently in experimental phase and a complete rewrite is in process to make it modular.
