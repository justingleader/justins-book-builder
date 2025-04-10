## Reference: Dates

Source: [Quarto Dates and Date Formatting – Quarto](https://quarto.org/docs/reference/dates.html)

### Date Parsing

When you write a date for Quarto document, Quarto will attempt to parse a date string by trying a number of standard forms before ultimately attempting to infer the date format. Quarto will try dates formatted as follows, in the following order:

*   MM/dd/yyyy
*   MM-dd-yyyy
*   MM/dd/yy
*   MM-dd-yy
*   yyyy-MM-dd
*   dd MM yyyy
*   MM dd, yyyy
*   YYYY-MM-DDTHH:mm:ssZ

In addition, you may also provide date keywords, which will provide a dynamic date.

| Keyword        | Date                                                        |
| :------------- | :---------------------------------------------------------- |
| `today`        | The current local date, with the time portion set to 0.     |
| `now`          | The current local date and time.                            |
| `last-modified`| The last modified date and time of the input file containing the date. |

### Date Formatting

When specifying a date format in Quarto, there are two ways to represent the format that you’d like.

#### Using a Date Style

You can specify a simple date style which will be used to format the date.

For example:

```yaml
---
date: 03/07/2005
date-format: long
---
```

Valid styles and examples of the formatted output are as follows:

| Style    | Description                             | Example             |
| :------- | :-------------------------------------- | :------------------ |
| `full`   | A full date that includes the weekday name | Monday, March 7, 2005 |
| `long`   | A long date that includes a wide month name | March 7, 2005       |
| `medium` | A medium date                           | Mar 7, 2005         |
| `short`  | A short date with a numeric month       | 3/7/05              |
| `iso`    | A short date in ISO format              | 2005-03-07          |

#### Using a Date Format

You can also specify a date format string that will be used to format the date. For example:

```yaml
---
date: 03/07/2005
date-format: "MMM D, YYYY"
```

The permissible values in this string include:

| Format String | Output            | Description                                            |
| :------------ | :---------------- | :----------------------------------------------------- |
| `YY`          | 18                | Two-digit year                                         |
| `YYYY`        | 2018              | Four-digit year                                        |
| `M`           | 1-12              | The month, beginning at 1                              |
| `MM`          | 01-12             | The month, 2-digits                                    |
| `MMM`         | Jan-Dec           | The abbreviated month name                             |
| `MMMM`        | January-December  | The full month name                                    |
| `D`           | 1-31              | The day of the month                                   |
| `DD`          | 01-31             | The day of the month, 2-digits                         |
| `d`           | 0-6               | The day of the week, with Sunday as 0                  |
| `dd`          | Su-Sa             | The min name of the day of the week                    |
| `ddd`         | Sun-Sat           | The short name of the day of the week                  |
| `dddd`        | Sunday-Saturday   | The name of the day of the week                        |
| `H`           | 0-23              | The hour                                               |
| `HH`          | 00-23             | The hour, 2-digits                                     |
| `h`           | 1-12              | The hour, 12-hour clock                                |
| `hh`          | 01-12             | The hour, 12-hour clock, 2-digits                      |
| `m`           | 0-59              | The minute                                             |
| `mm`          | 00-59             | The minute, 2-digits                                   |
| `s`           | 0-59              | The second                                             |
| `ss`          | 00-59             | The second, 2-digits                                   |
| `SSS`         | 000-999           | The millisecond, 3-digits                              |
| `Z`           | +05:00            | The offset from UTC, ±HH:mm                            |
| `ZZ`          | +0500             | The offset from UTC, ±HHmm                             |
| `A`           | AM PM             |                                                        |
| `a`           | am pm             |                                                        |
| `Q`           | 1-4               | Quarter                                                |
| `Do`          | 1st 2nd … 31st    | Day of Month with ordinal                              |
| `k`           | 1-24              | The hour, beginning at 1                               |
| `kk`          | 01-24             | The hour, 2-digits, beginning at 1                     |
| `X`           | 1360013296        | Unix Timestamp in second                               |
| `x`           | 1360013296123     | Unix Timestamp in millisecond                          |
| `w`           | 1 2 … 52 53       | Week of year ( dependent WeekOfYear plugin )          |
| `ww`          | 01 02 … 52 53     | Week of year, 2-digits ( dependent WeekOfYear plugin ) |
| `W`           | 1 2 … 52 53       | ISO Week of year ( dependent IsoWeek plugin )          |
| `WW`          | 01 02 … 52 53     | ISO Week of year, 2-digits ( dependent IsoWeek plugin )|
| `wo`          | 1st 2nd … 52nd 53rd | Week of year with ordinal ( dependent WeekOfYear plugin ) |
| `gggg`        | 2017              | Week Year ( dependent WeekYear plugin )                |
| `GGGG`        | 2017              | ISO Week Year ( dependent IsoWeek plugin )             |
| `z`           | EST               | Abbreviated named offset ( dependent Timezone plugin )   |
| `zzz`         | Eastern Standard Time | Unabbreviated named offset ( dependent Timezone plugin ) |

To escape characters, wrap them in square brackets (e.g. `[MM]`).

Example formats and outputs include:

| Format                            | Output                          |
| :-------------------------------- | :------------------------------ |
| `MMM D, YYYY`                     | Mar 7, 2005                     |
| `DD/MM/YYYY`                      | 07/03/2005                      |
| `[YYYYescape] YYYY-MM-DDTHH:mm:ssZ[Z]` | YYYYescape 2005-03-07T00:00:00-05:00Z |
| `YYYY-MM-DDTHH:mm:ssZ`            | 2005-03-07T00:00:00-05:00       |
| `dddd MMM D, YYYY`                | Monday Mar 7, 2005              |

