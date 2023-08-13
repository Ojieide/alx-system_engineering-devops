# 0x19. Postmortem

![meme](https://github.com/Ojieide/alx-system_engineering-devops/assets/47607681/731cf4c6-55f7-472c-a690-fee8d55609fd)

## Issue Summary
  * Duration of outage: August 10, 2022, 09:00 AM UTC to August 10, 2022, 01:00 PM UTC.
  * Impact: 100% of users were unable to access any of the core applications hosted on our
    HPE ProLiant DL380 Gen10 server running Windows Server 2012 R2 operating system.
  * Root cause: Microsoft iSCSI Initiator name was changed without updating the Favourite
    Target entries.
	
## Timeline
  * August 10, 2022, 09:00 AM UTC.
  * Users complained that they were unable to access any of the core applications.
  * The assumption was that the host did not have internet access and could not communicate
    with other computers or network devices so a ping was sent to the host ip address and
    it was successful.
  * The team spent several hours debugging the issue. They restarted the internet connection,
    cleared the broswer cache, disabled the firewall, flushed the dns cache and changed the
    dns servers but the applications were still inaccessible.
  * The incident was escalated to the Systems Administrator.
  * The incident was resolved by conducting a comprehensive investigation of the host server.
  
## Root cause and resolution
  * When a Favorite Target entry is created, the iSCSI Initiator sets the Favorite Target
    entry to use the Initiator Name that is configured at the time of creation. If the
    Initiator Name is later changed, any pre-existing Favorite Target entries are not
    updated to reflect the newly configured Initiator Name.
  * When the Initiator Name is changed in the iSCSI Initiator Properties, any pre-existing
    Favorite Target entries should be removed and recreated to ensure they use the new
    Initiator Name. Also, ensure the Initiator Name always matches the Initiator Name that
    the iSCSI target is using for access control.

## Corrective and preventative measures
  * Setup a monitoring alert that alerts the team anytime an application is inaccessible.
  * When the Initiator Name is changed in the iSCSI Initiator Properties, any pre-existing
    Favorite Target entries should be removed and recreated to ensure they use the new
    Initiator Name. Also, ensure the Initiator Name always matches the Initiator Name that
    the iSCSI target is using for access control.
