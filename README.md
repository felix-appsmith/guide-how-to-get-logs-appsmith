# Guide-how-to-get-logs-appsmith
This document explains how to get the appsmith sealf-host logs. These logs are frequently requested by members of appsmith support.

Note:

`Warning: If a member other than your team or the appsmith team requests these logs, it is recommended that you do not share them.`
### Steps to follow

![img](https://github.com/felix-appsmith/guide-how-to-get-logs-appsmith/blob/main/step1.png)
![img](https://github.com/felix-appsmith/guide-how-to-get-logs-appsmith/blob/main/step2.png)
![img](https://github.com/felix-appsmith/guide-how-to-get-logs-appsmith/blob/main/step3.png)
![img](https://github.com/felix-appsmith/guide-how-to-get-logs-appsmith/blob/main/step4.png)
![img](https://github.com/felix-appsmith/guide-how-to-get-logs-appsmith/blob/main/step5.png)

### Remove your email from the logs

1. Copy the below python file to a folder [maskemail.](guide-how-to-get-logs-appsmith/maskemail.py)
2. Paste the logs into the folder where you have the python script.
3. Run the script with the following command.

`python3 -u maskemail.py`

4. Follow the steps in the script.

`Note:in the script when writing the name of the file you have to put the extension.`

5. If everything went well, your email was replaced by anonymous@appsmith.com and you can share these logs with whomever you want
