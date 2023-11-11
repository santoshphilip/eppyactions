2023-11-11
==========

mac install on CI is not running. Try to install on older mac OS [10 rather than 12]
2023-11-10
==========

try running with two installs

2023-11-09
==========

github actions:

- install for E+ worked for
    - E+ version 22.2
    - Ubuntu-20.04
- install for E+ failed for
    - E+ version 22.2
    - Ubuntu-22.04

both ./github/workflows/main.yml and ./github/workflows/install.sh have to be updated to reflect the above two installs.

    
Next step
---------

- have a setup file where version number can be set.
- hard todo -
    - two files have to be updated
    - might have to do by hand.
    - local testing may have to be done from a different place.

There is away to do this.

- set these two varibles in ``input:`` at the top of the mail.yml file
- install.sh will pick it as an os.inviron() type of input
- make sure that you set the variables in ``env:`` at the right place in mail.yml
- for local test read it off from mail.yml
