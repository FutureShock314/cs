# Tests

| Testing what?  | input, {type}, {in}     | Expected out         | Actual out        | did it work? |
|:--------------:|:-----------------------:|:--------------------:|:-----------------:|:------------:|
| username check | erroneous, a            | username no exist    | username no exist | yeah i think |
| username check | normal, user            | Password?            | Password?         | yeah i think |
| pass check     | erroneous, cheese       | no lol               | no lol            | probably     |
| pass check     | normal, password        | ok                   | ok                | probably     |
| weather        | { none }                | { the weather }      | { the weather }   | i believe so |
| news           | { none for first }      | { top 10 headlines } | { that }          | sure did     |
| news specific  | erroneous, { a LIVE }   | { err: no live }     | { err: no live }  | yessir       |
| news specific  | boundary, 11            | { prompt again }     | { prompt again }  | yessir       |
| news specific  | normal, 6               | { the article }      | { the article }   | yessir       |
