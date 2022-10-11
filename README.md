# Guide: How to get logs on Appsmith

This document will guide you on how to get the logs Appsmith on self-hosted deployments (such as Docker). These logs are frequently requested by members of the Appsmith Support team to properly troubleshoot bugs.

`Warning: If a member other than your team or the appsmith team requests these logs, it is recommended that you do not share them.`

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

1. Copy the below Python file to a folder [maskemail.](guide-how-to-get-logs-appsmith/maskemail.py)
2. Paste the logs into the folder where you have the python script.
3. Run the script with the following command.

`python3 -u maskemail.py`

4. Follow the steps in the script.

`Note:in the script when writing the name of the file you have to put the extension.`

5. If everything went well, your email was replaced by anonymous@appsmith.com and you can share these logs with whomever you want
