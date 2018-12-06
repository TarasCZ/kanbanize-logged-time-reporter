Kanbanize Logged Time Reporter

Are you tired of going through all cards in kanbanize in order to check your logged hours?
Then you can use my little script.

USAGE:

1. Edit config.json
    - `username`: your Kanbanize username
    - `domain`: if your company has URL `yourcompany.kanbanize.com` then `yourcompany` is your domain
    - `api-key`: you can find your API key in Kanbanize by clicking on your profile piture (right top corner) > API
    - `date`: use YYYY-MM-DD format
        - `date to`: if you want to see report until (for example) 15th set this value to 16th, for report including last day of the month set the first day of the next month

2. Run ShowMeReport.py (python3 ShowMeReport.py)