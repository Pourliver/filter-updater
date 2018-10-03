# Filter-Updater for Path of Exile
__ONLY TESTED ON WINDOWS, USE AT YOUR OWN RISK__

This python script installs the latest version of NeverSink's itemfilter for Path of Exile.

### Installation 

To install, run the following command
```bash
git clone https://github.com/Pourliver/filter-updater.git
```

The script depends on `beautifulsoup4`. You can install it like this.
```bash
pip install beautifulsoup4
```

### Example
To start the updater, double click the python file or type the following.

`python update-filter.py`

This would output something like this.

![Example](https://i.imgur.com/Nynmce2.png "Example")

You can edit the following variables to change the default filter location.
```python
#Default install path on Windows
current_user_path = os.environ["USERPROFILE"]
folder_location = current_user_path + "\Documents\My Games\Path of Exile"
```