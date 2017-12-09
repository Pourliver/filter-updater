# Filter-Updater
__ONLY TESTED ON WINDOWS, USE AT YOUR OWN RISK__


Install the latest version of NeverSink's itemfilter for Path of Exile.

You can edit the following variables to change the default filter location.
```python
#Default install path on Windows
current_user_path = os.environ["USERPROFILE"]
folder_location = current_user_path + "\Documents\My Games\Path of Exile"
```

To start the updater, double click the python file or type the following.

`python update-filter.py`

If dependencies are missing, run the following command as admin.

```bash
pip install beautifulsoup4
```
