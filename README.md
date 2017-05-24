# stocshare
For stock and finance analysis
{
    "shell_cmd": "C:/Anaconda2/python.exe -u \"$file\"",
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",

    "env": {"PYTHONIOENCODING": "utf-8"},

    "variants":
    [
        {
            "name": "Syntax Check",
            "shell_cmd": "C:/Anaconda2/python.exe -m py_compile \"${file}\"",
        }
    ]
}
