# Guide: How to get logs on Appsmith

This document will guide you on how to get the logs Appsmith on self-hosted deployments (such as Docker). These logs are frequently requested by members of the Appsmith Support team to properly troubleshoot bugs.

**A few words on logs and privacy**: 

- Appsmith's logs usually don't contain information that should be considered "risky" to share. But if you want/are required to remove any PII, please refer to the section bellow called "Procedure: Removing PII from logs".
- It is best to share your logs directly to the Appsmith Support Team via the official support channels.

## Procedure: How to get the Backend logs

### Step 1

Look for the folder from where you deployed Appsmith. On this example we will assume that Appsmith was deployed using the official `docker-compose.yaml` and that file is located on a folder called `Appsmith` on the Desktop.

![img](https://github.com/felix-appsmith/guide-how-to-get-logs-appsmith/blob/main/step1.png)

### Step 2

Locate the `stacks` folder.

![img](https://github.com/felix-appsmith/guide-how-to-get-logs-appsmith/blob/main/step2.png)

### Step 3

Go to the `logs` folder.

![img](https://github.com/felix-appsmith/guide-how-to-get-logs-appsmith/blob/main/step3.png)

### Step 4

In this case move to the `backend` folder.

![img](https://github.com/felix-appsmith/guide-how-to-get-logs-appsmith/blob/main/step4.png)

### Step 5

There you will find one or many `.log` files. If you want to remove any PII from the logs follow the section below called [Procedure: Removing PII from log files](). If that's not a concer please bundle those files on a `.zip` file and share it with the Appsmith Team.

![img](https://github.com/felix-appsmith/guide-how-to-get-logs-appsmith/blob/main/step5.png)

## Procedure: Removing PII from log files

1. Copy the below Python file to a folder [maskdata.](guide-how-to-get-logs-appsmith/maskdata.py)
2. Install the dependencies.

```console
pip install scrubadub
```

3. Execute the script with the command.
```console
python3 -u maskemail.py
```
4. The script requested the name of the file, type the name with the file extension and the program will replace the sensitive data.

5. This script was built from the following [library.](https://github.com/LeapBeyond/scrubadub)

`Note: The script and log file must be in the same folder.`

``scrubadub`` currently supports removing:

* Names
* Email addresses
* Addresses/Postal codes (US, GB, CA)
* Credit card numbers
* Dates of birth
* URLs
* Phone numbers
* Username and password combinations
* Skype/twitter usernames
* Social security numbers (US and GB national insurance numbers)
* Tax numbers (GB)
* Driving licence numbers (GB)
