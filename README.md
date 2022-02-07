# auto bank data gatherer
this project uses pyautogui and pyperclip to use your normal browsing browser and password manager to move your mouse and keyboard to login to various banks and institutions and scrape your data and output it to a log file.

## supported OS's
* windows 10

## supported browsers
* edge

## supported password managers
* bitwarden edge extension - need to be already logged in to the extension for this to work

## disclaimers
* this project assumes that you have recently logged into these services and will not handle cell phone auth to ensure you can log in. Only simple username and password login
* can not handle bitwarden's mfa token generating facilities yet
* pyautogui WILL take over your mouse and keyboard, to try to force it to escape move your mouse to the upper corner of the screen

## features and roadmap
- [x] output data as csv
- [ ] output data as json
- [x] site wide config file
- [ ] log runs in a log file
- [ ] take a snapshot pdf of each site run
- [ ] cli usage, output to cli only and/or output specific site data only
- [ ] cleanly iterate through each account data
- [ ] handle bitwarden auto MFA
- [ ] rotate passwords for user, ensure new password is saved to password manager, ensure old password is saved as a note appended to the rest of the note data
- [ ] simple data visualization by time and account, and aggregate data accross accounts

## supported sites
- [x] ally bank
- [x] schwab brokerage
- [ ] fidelity brokerage - IN PROGRESS
- [ ] honda financial
- [ ] discover card
- [ ] citi bank
- [ ] td bank card

## TODO
- fix browser tabs not closing after ally and schwab runs