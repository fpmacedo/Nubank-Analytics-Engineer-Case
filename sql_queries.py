# DROP TABLES

accounts_table_drop = "DROP TABLE IF EXISTS accounts_table;"
city_table_drop = "DROP TABLE IF EXISTS city_table;"
costumers_table_drop = "DROP TABLE IF EXISTS costumers_table;"
country_table_drop = "DROP TABLE IF EXISTS country_table;"
d_month_table_drop = "DROP TABLE IF EXISTS d_month_table;"
d_time_table_drop = "DROP TABLE IF EXISTS d_time_table;"
d_week_table_drop = "DROP TABLE IF EXISTS d_week_table;"
d_weekday_table_drop = "DROP TABLE IF EXISTS d_weekday_table;"
d_year_table_drop = "DROP TABLE IF EXISTS d_year_table;"
pix_movements_table_drop = "DROP TABLE IF EXISTS pix_movements_table;"
state_table_drop = "DROP TABLE IF EXISTS state_table;"
transfer_ins_table_drop = "DROP TABLE IF EXISTS transfer_ins_table;"
transfer_outs_table_drop = "DROP TABLE IF EXISTS transfer_outs_table;"

# CREATE TABLES

accounts_table_create = ("""CREATE TABLE IF NOT EXISTS accounts_table 
                            (   account_id             uuid PRIMARY KEY,
                                customer_id            uuid,
                                created_at             timestamp,
                                status                 varchar(128),
                                account_branch         varchar(128),
                                account_check_digit    varchar(128),
                                account_number         varchar(128)
                            );"""
                        )

city_table_create = ("""CREATE TABLE IF NOT EXISTS city_table
                        (
                            city_id     int PRIMARY KEY,
                            city        varchar(256),
                            state_id    uuid
                            
                        );"""
                    )

costumers_table_create = ("""CREATE TABLE IF NOT EXISTS costumers_table
                        (
                        customer_id      uuid PRIMARY KEY,
                        first_name       varchar(128),
                        last_name        varchar(128),
                        customer_city    int,
                        cpf              int,
                        country_name     varchar(128)
                        );"""
                    )

country_table_create = ("""CREATE TABLE IF NOT EXISTS country_table
                          (
                            country_id      uuid PRIMARY KEY,
                            country         varchar(128)
                          );"""
                      )

d_month_table_create = ("""CREATE TABLE IF NOT EXISTS d_month_table
                        (
                            month_id        int PRIMARY KEY,
                            action_month    int
                        );"""
                    )

d_time_table_create = ("""CREATE TABLE IF NOT EXISTS d_time_table
                        (
                            time_id             int PRIMARY KEY,
                            action_timestamp    timestamp,
                            week_id             int,
                            month_id            int,
                            year_id             int,
                            weekday_id          int
                        );"""
                    )

d_week_table_create = ("""CREATE TABLE IF NOT EXISTS d_week_table
                        (
                            weekday_id          int PRIMARY KEY,
                            action_week         int
                        );"""
                    )

d_weekday_table_create = ("""CREATE TABLE IF NOT EXISTS d_weekday_table
                        (
                            weekday_id          int PRIMARY KEY,
                            action_weekday      varchar(128)
                        );"""
                    )

d_year_table_create = ("""CREATE TABLE IF NOT EXISTS d_year_table
                        (
                            year_id             int PRIMARY KEY,
                            action_year         int
                        );"""
                    )

pix_movements_table_create = ("""CREATE TABLE IF NOT EXISTS pix_movements_table
                        (
                            id                  uuid PRIMARY KEY,
                            account_id          uuid,
                            in_or_out           varchar(128),
                            pix_amount          float,
                            pix_requested_at    int,
                            pix_completed_at    int,
                            status              varchar(128)
                        );"""
                    )

state_table_create = ("""CREATE TABLE IF NOT EXISTS state_table
                        (
                            state_id            uuid PRIMARY KEY,
                            state               varchar(128),
                            country_id          uuid
                        );"""
                    )

transfer_ins_table_create = ("""CREATE TABLE IF NOT EXISTS transfer_ins_table
                        (
                            id                          uuid PRIMARY KEY,
                            account_id                  uuid,
                            amount                      float,
                            transaction_requested_at    int,
                            transaction_completed_at    int,
                            status                      varchar(128)
                        );"""
                    )

transfer_outs_table_create = ("""CREATE TABLE IF NOT EXISTS transfer_outs_table
                        (
                            id                          uuid PRIMARY KEY,
                            account_id                  uuid,
                            amount                      float,
                            transaction_requested_at    int,
                            transaction_completed_at    int,
                            status                      varchar(128)
                        );"""
                    )

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay_table
                            (
                            start_time,
                            user_id,
                            level,
                            song_id,
                            artist_id,
                            session_id,
                            location,
                            user_agent
                            ) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
                        )

user_table_insert = ("""INSERT INTO user_table
                        (
                        user_id,
                        first_name,
                        last_name,
                        gender,
                        level
                        ) 
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;"""
                    )

song_table_insert = ("""INSERT INTO song_table
                        (
                        song_id,
                        title,
                        artist_id,
                        year,
                        duration
                        )
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (song_id) DO NOTHING;"""
                    )

artist_table_insert = ("""INSERT INTO artist_table
                          (
                          artist_id,
                          name,
                          location,
                          latitude,
                          longitude
                          )
                          VALUES (%s, %s, %s, %s, %s)
                          ON CONFLICT (artist_id) DO NOTHING;"""
                      )


time_table_insert = ("""INSERT INTO time_table
                        (
                        start_time,
                        hour,
                        day,
                        week,
                        month,
                        year,
                        weekday
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (start_time) DO NOTHING;"""
                    )

# FIND SONGS

song_select = ("""SELECT 
                  song_table.song_id, artist_table.artist_id
                  FROM 
                  song_table JOIN artist_table ON (song_table.artist_id = artist_table.artist_id)
                  WHERE 
                  song_table.title = %s AND artist_table.name = %s AND song_table.duration = %s;"""
              )

# QUERY LISTS

create_table_queries = [accounts_table_create, city_table_create, costumers_table_create,country_table_create, d_month_table_create, d_time_table_create, 
d_week_table_create, d_year_table_create, pix_movements_table_create, state_table_create, transfer_ins_table_create, transfer_outs_table_create] #, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [accounts_table_drop] #, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]