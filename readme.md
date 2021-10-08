# Eating Schedule Reminder of HKUST

## Data source

We sample data from [**Pulse of HKUS**](http://pulse-api.hkustvis.org/). 

## Notification APP setup

We use [Bark](https://github.com/Finb/Bark). Setup and installation can be found in their repo.

You can pass your Bark key by creating a file named `barkKey.py` with a single line inside:

```python
barkKey = "Your_Bark_Key"
```

Then add execution permission to the script by

```shell
chmod +x ./script.sh
```



## Crontab Setup

Use `crontab -e` to setup crontab, add these lines

```shell
*/5 11-13 * * 1-5 /home/user/path/to/script
# every 5th min at each hour of 11:00 to 13:00 at every weekday
*/5 17-18 * * 1-5 /home/user/path/to/script
# every 5th min at each hour of 17:00 to 18:00 at every weekday
```

for reference see [corntab guru](https://crontab.guru/examples.html).

