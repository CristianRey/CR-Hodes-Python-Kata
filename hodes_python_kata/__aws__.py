'''
Program designed to retrieve objects from a AWS S3 location.
It asks the user for certain information:
1. Keys to login.
2. Bucket name.
3. Object key.
'''
import boto
import boto.s3.connection
import os.path
import getpass
import csv
import sys
import re

class constants():
    def requiredinfo(self):
        return 'You will need the following: access_key, secret_key, bucket name, and the file key, Continue? (y/n): '

    def enterkey(self):
        return 'Please enter AWS Key or enter c to cancel: '

    def entersecretkey(self):
        return 'Please enter AWS Secret Key or enter c to cancel: '

    def enterbucketname(self):
        return 'Please enter bucket name (case sensitive) or enter c to cancel: '

    def enterkeyname(self):
        return 'Please enter object key name with slashes if necessary (case sensitive) or enter c to cancel: '

    def checkcredentials(self):
        return 'Error opening connection to AWS S3. Please check your credentials and try again'

    def filealreadyexists(self):
        return 'File already exists, override? (y/n): '

    def invalidbucketnameperiod(self):
        return "Bucket name cannot start or end with a period."

    def invalidbucketnamedash(self):
        return "Bucket name cannot end with a dash."

    def invalidbucketnameperiods(self):
        return "Bucket name cannot contain two consecutive periods."

    def invalidbucketnameperioddash(self):
        return "Bucket name cannot contain a period and a dash consecutively."

    def invalidbucketnamecharacters(self):
        return "Invalid bucket name, bucket name cannot contain any of these special characters !-_.*'()"

    def invalidbucketnameipaddress(self):
        return "Invalid bucket name, bucket name cannot be formatted as an IP address"


messages = constants()

def mergemanager(filepath, usermsg, userchoice):
    merge = raw_input(usermsg + userchoice + '), merge them together (m), or cancel (c) ? (' + userchoice + '/m/c): ')

    while (merge != userchoice and merge != 'm' and merge != 'c'):
        merge = raw_input(usermsg + userchoice + '), merge them together (m), or cancel (c) ? (' + userchoice + '/m/c): ')

    if (merge == 'c'):
        exit()

    elif (merge == userchoice):
        # Now download the file from AWS S3
        downloadfile(key, filepath)
    elif (merge == 'm'):
        # First merge the file in the hard drive to the merged file.
        if (mergefiles(filepath, filepath.replace(".csv", "_merged.csv"))):
            # Now download the file from AWS S3
            if (downloadfile(key, filepath)):
                # Now merge the file that was just downloaded
                mergefiles(filepath, filepath.replace(".csv", "_merged.csv"))

                print 'Files merged successfully into ' + filepath.replace(".csv", "_merged.csv")

def downloadfile (key, filepath):
    try:
        if (os.path.isfile(filepath)):
            os.remove(filepath)

        key.get_contents_to_filename(filepath)

    except IOError as IOe:
        print "I/O error({0}): {1}".format(IOe.errno, IOe.strerror)

    except Exception as e:
        print "Unexpected error:", str(e)

    else:
        print 'File ' + filepath + ' downloaded successfully.'
        return True

def mergefiles (filepath, destpath):
    # This function may get called if there is no contacts.csv file in the directory. Check that the file exists first.
    try:
        if (os.path.isfile(filepath)):
            with open(filepath, 'rU') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

                mode = ""

                if os.path.isfile(destpath):
                    mode="a"
                else:
                    mode="w"

                file = open(destpath, mode)
                dest = csv.writer(file)

                for row in spamreader:
                    dest.writerow(row)

                file.close()

            os.remove(filepath)

    except IOError as IOe:
        print "I/O error({0}): {1}".format(IOe.errno, IOe.strerror)
        return False

    except:
        print "Unexpected error:", sys.exc_info()[0]
        return False

    else:
        return True

def countlines (filepath):
    iCounter = 0

    with open(filepath, 'rU') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for row in spamreader:
            iCounter = iCounter + 1

    print "File " + " contains " + str(iCounter) + " rows."

def validatebucket(bucket):
    ip_match = re.match('^' + '[\.]'.join(['(\d{1,3})'] * 4) + '$', bucket)
    ip_validate = bool(ip_match)
    if ip_validate:
        messages.invalidbucketnameipaddress()
        return False

    for c in bucket:
        if ("!-_.*'()".__contains__(c)):
            print (messages.invalidbucketnamecharacters())
            return False

    return True

OK = raw_input(messages.requiredinfo()).lower().strip()

while (OK!='y' and OK!='n'):
    OK = raw_input(messages.requiredinfo()).lower().strip()

if (OK=='n'):
    exit()

access_key = raw_input(messages.enterkey()).strip()

if (access_key == 'c'):
    exit()

while (access_key.__len__()==0):
    access_key = raw_input(messages.enterkey()).strip()

    if (access_key=='c'):
        exit()

secret_key = raw_input(messages.entersecretkey()).strip()

if (secret_key=='c'):
    exit()

while (secret_key.__len__()==0):
    secret_key = raw_input(messages.entersecretkey()).strip()

    if (secret_key=='c'):
        exit()

bucketname = raw_input(messages.enterbucketname()).strip()

if (bucketname=='c'):
    exit()

while (bucketname.__len__()==0):
    bucketname = raw_input(messages.enterbucketname()).strip()

    if (bucketname == 'c'):
        exit()

# validate
if(validatebucket(bucketname)==False):
    exit()

filekey = raw_input(messages.enterkeyname()).strip()

while (filekey.__len__()==0):
    filekey = raw_input(messages.enterkeyname).strip()

if (filekey == 'c'):
    exit()

if (filekey.endswith("/")):
    print ("Invalid object name " + filekey)
    exit()

while (filekey.startswith("/")):
    filekey = filekey[1:filekey.__len__()]

if (filekey.find("/")):
    targetfile = filekey.split("/")

    filepath='/Users/' + getpass.getuser() + '/Downloads/' + targetfile[len(targetfile)-1] # Untitled.rtf'
else:
    filepath='/Users/' + getpass.getuser() + '/Downloads/' + filekey # Untitled.rtf'

try:
    conn = boto.connect_s3(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        # host='objects.dreamhost.com',
        is_secure=False,               # uncomment if you are not using ssl
        calling_format=boto.s3.connection.OrdinaryCallingFormat(),
    )
except Exception as e:
    print messages.checkcredentials, str(e)

else:
    blnBucketFound = False
    blnKeyFound = False

    try:
        for bucket in conn.get_all_buckets():
            if (bucket.name == bucketname):
                blnBucketFound = True

                blnKeyFound = False

                for key in bucket.list():

                    if (key.name == filekey): #'horror/Untitled.rtf'):
                        blnKeyFound = True

                        key = bucket.get_key(key.name)

                        if (not (os.path.isfile(filepath))):
                            if (key.name.endswith(".csv") and os.path.isfile(filepath.replace(".csv", "_merged.csv"))):
                                mergemanager(filepath, 'Merged file already exists, download the new file only (','d')
                            else:
                                downloadfile(key, filepath)
                        else:
                            # print filecontents.count("\n")
                            if (key.name.endswith(".csv")):
                                mergemanager(filepath, 'File already exists, override existing (', 'o')
                            else:
                                override = raw_input((messages.filealreadyexists()))

                                override = override.lower().strip()

                                while (override != 'y' and override != 'n'):
                                    override = raw_input((messages.filealreadyexists()).lower())

                                if (override == 'y'):
                                    downloadfile(key, filepath)
                                else:
                                    print 'File already exists'

                        break

                        if (blnBucketFound):
                            break
    except Exception as e:
        print messages.checkcredentials(), str(e) #sys.exc_info()[0]

if (blnBucketFound == False):
    print "Bucket " + bucketname + " was not found."

if (blnKeyFound == False):
    print "Key " + filekey + " was not found."
