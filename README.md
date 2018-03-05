python version conflictions
library conflictions
small issues like root access
some processes should be with root access and some not
folders with same name should be renamed before download
sync at startup
we don't have a tree on cloud
watch files
concurrent access
choose appropriate locations
rename or move the files on desktop doesn't change innode no
###################
#get states of file
stat
exiftool filename
find /home/prateek/Google\ Drive -type f -printf '%TY-%Tm-%Td %TT %p\n' | sort -r
###################

###################
#get checksum of filename (* for all)
md5sum filename > checklist.chk
###################



**google drive folder:**
    
    /home/$USER/google drive

**icon for startmenu and desktop:**
    
    /usr/share/icons

**shortcut for startmenu:**
    
    /usr/share/applications

**nautilus bookmark make entry in:**
    
    /home/$USER/.config/gtk-3.0/bookmarks

**startup entry:**
    
    /home/$USER/.config/autostart/clouddrive/cloud drive.desktop

**credentials:**

    /etc/credentials/credentials.json

**clouddrive command:**

    /usr/local/bin/clouddrive

**Installation folder:**
    
    /usr/local/apps/cloud drive

**settings:**

    /home/$USER/.clouddrive
    
**desktop tree example:**

    {
      "file1": {
        "mimeType": "file",
        "innodeNo": 1
      },
      "file2": {
        "mimeType": "file",
        "innodeNo": 2
      },
      "folder1": {
        "mimeType": "inode/directory",
        "innodeNo": 3,
        "children": {
          "file2": {
            "mimeType": "file",
            "innodeNo": 2
          },
          "folder2": {
            "mimeType": "inode/directory",
            "innodeNo": 5,
            "children": false
          }
        }
      }
    }