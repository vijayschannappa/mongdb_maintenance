

service = "mongod"

filepath = '/var/lib/mongodb/mongod.lock'


def check_and_start_mongo():
    # print('called function')
    # proces = subprocess.Popen(
    #     ["systemctl", "is-active", service], stdout=subprocess.PIPE)
    # (output, err) = proces.communicate()
    stat_command = 'sudo service mongod status'
    output = subprocess.check_output(['bash', '-c', stat_command])
    output = output.decode('utf-8')
    print(f'output:{output}')
    if 'start/running' in output:
        print('mongo active')
        sys.exit()
    else:
        repair_mongo()


def repair_mongo():
    if os.path.isfile(filepath):
        os.remove(filepath)
        start_mongo_again()
    else:
        print('mongo fucked up with some other problem')
        comand = 'sudo service mongod start'
        subprocess.check_output(['bash', '-c', comand])
        alert = f"Mongod service stopped at {datetime.now()} but restarted succesfully"
        mongo_alert.alert_mail_sender(alert)
        sys.exit()


def start_mongo_again():
    bashcommand = "sudo service mongod restart"
    subprocess.check_output(['bash', '-c', bashcommand])
    alert = f"Mongod service stopped due to unclean shutdown, removed lock file and restarted mongodb succesfully"
    mongo_alert.alert_mail_sender(alert)
    sys.exit()


if __name__ == '__main__':
    import subprocess
    import sys
    import os
    from datetime import datetime
    import mongo_alert
    check_and_start_mongo()
