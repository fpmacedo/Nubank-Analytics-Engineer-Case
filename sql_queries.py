# DROP TABLES

accounts_table_drop = "DROP TABLE IF EXISTS accounts_table;"
city_table_drop = "DROP TABLE IF EXISTS city_table;"
customers_table_drop = "DROP TABLE IF EXISTS customers_table;"
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
fact_movements_table_drop = "DROP TABLE IF EXISTS fact_movements_table;"
dim_time_table_drop = "DROP TABLE IF EXISTS dim_time_table;"
dim_customers_table_drop = "DROP TABLE IF EXISTS dim_customers_table;"

# CREATE TABLES

accounts_table_create = ("""CREATE TABLE IF NOT EXISTS accounts_table 
                            (   account_id             bigint PRIMARY KEY,
                                customer_id            bigint,
                                created_at             timestamp,
                                status                 varchar(128),
                                account_branch         varchar(128),
                                account_check_digit    varchar(128),
                                account_number         varchar(128)
                            );"""
                        )

city_table_create = ("""CREATE TABLE IF NOT EXISTS city_table
                        (
                            city        varchar(256),
                            state_id    bigint,
                            city_id     bigint PRIMARY KEY                
                        );"""
                    )

customers_table_create = ("""CREATE TABLE IF NOT EXISTS customers_table
                        (
                        customer_id      bigint PRIMARY KEY,
                        first_name       varchar(128),
                        last_name        varchar(128),
                        customer_city    bigint,
                        cpf              bigint,
                        country_name     varchar(128)
                        );"""
                    )

country_table_create = ("""CREATE TABLE IF NOT EXISTS country_table
                          (
                            country_id      bigint PRIMARY KEY,
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
                            time_id             bigint PRIMARY KEY,
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
                            id                  bigint PRIMARY KEY,
                            account_id          bigint,
                            in_or_out           varchar(128),
                            pix_amount          float,
                            pix_requested_at    varchar(256),
                            pix_completed_at    varchar(256),
                            status              varchar(128)
                        );"""
                    )

state_table_create = ("""CREATE TABLE IF NOT EXISTS state_table
                        (
                            state_id            bigint PRIMARY KEY,
                            state               varchar(128),
                            country_id          bigint
                        );"""
                    )

transfer_ins_table_create = ("""CREATE TABLE IF NOT EXISTS transfer_ins_table
                        (
                            id                          bigint PRIMARY KEY,
                            account_id                  bigint,
                            amount                      float,
                            transaction_requested_at    varchar(256),
                            transaction_completed_at    varchar(256),
                            status                      varchar(128)
                        );"""
                    )

transfer_outs_table_create = ("""CREATE TABLE IF NOT EXISTS transfer_outs_table
                        (
                            id                          bigint PRIMARY KEY,
                            account_id                  bigint,
                            amount                      float,
                            transaction_requested_at    varchar(256),
                            transaction_completed_at    varchar(256),
                            status                      varchar(128)
                        );"""
                    )

fact_movements_table_create = ("""CREATE TABLE IF NOT EXISTS fact_movements_table
                        (
                            id                  bigint PRIMARY KEY,
                            account_id          bigint,
                            customer_id         bigint,
                            in_or_out           varchar(128),
                            type                varchar(128),
                            amount              float,
                            requested_at        varchar(256),
                            completed_at        varchar(256),
                            status              varchar(128)
                        );"""
                    )

dim_time_table_create = ("""CREATE TABLE IF NOT EXISTS dim_time_table
                        (
                            time_id             bigint PRIMARY KEY,
                            action_timestamp    timestamp,
                            action_week         int,
                            action_month        int,
                            action_year         int,
                            action_weekday      int
                        );"""
                    )

dim_customers_table_create = ("""CREATE TABLE IF NOT EXISTS dim_customers_table
                        (
                            customer_id      bigint PRIMARY KEY,
                            first_name       varchar(128),
                            last_name        varchar(128),
                            city,            varchar(128),
                            state            varchar(128),
                            country          varchar(128),
                            cpf              bigint
                            
                        );"""
                    )


# INSERT

accounts_table_insert = ("""INSERT INTO accounts_table
                            (
                            account_id,
                            customer_id,            
                            created_at,            
                            status,              
                            account_branch,         
                            account_check_digit,    
                            account_number         
                            ) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s);"""
                        )

city_table_insert = ("""INSERT INTO city_table
                        (
                            city_id,
                            city,
                            state_id
                            
                        ) 
                        VALUES (%s, %s, %s);"""
                    )

customers_table_insert = ("""INSERT INTO customers_table
                        (
                        customer_id,
                        first_name,
                        last_name,
                        customer_city,
                        cpf,
                        country_name
                        )
                        VALUES (%s, %s, %s, %s, %s, %s)
                        ON CONFLICT (customer_id) DO NOTHING;"""
                    )

country_table_insert = ("""INSERT INTO country_table
                          (
                            country_id,
                            country
                          )
                          VALUES (%s, %s)
                          ON CONFLICT (country_id) DO NOTHING;"""
                      )


d_month_table_insert = ("""INSERT INTO d_month_table
                        (
                        month_id,
                        action_month
                        )
                        VALUES (%s, %s)
                        ON CONFLICT (month_id) DO NOTHING;"""
                    )

d_time_table_insert = ("""INSERT INTO d_time_table
                        (
                            time_id,
                            action_timestamp,
                            week_id,
                            month_id,
                            year_id,
                            weekday_id
                        )
                        VALUES (%s, %s, %s, %s, %s, %s);"""
                    )

d_week_table_insert = ("""INSERT INTO d_week_table
                        (
                            weekday_id,
                            action_week
                        )
                        VALUES (%s, %s);"""
                    )

d_weekday_table_insert = ("""INSERT INTO d_weekday_table
                        (
                            weekday_id,
                            action_weekday
                        )
                        VALUES (%s, %s);"""
                    )

d_year_table_insert = ("""INSERT INTO d_year_table
                        (
                            year_id,
                            action_year
                        )
                        VALUES (%s, %s);"""
                    )

pix_movements_table_insert = ("""INSERT INTO pix_movements_table
                        (
                            id,
                            account_id,
                            in_or_out,
                            pix_amount,
                            pix_requested_at,
                            pix_completed_at,
                            status
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s);"""
                    )

transfer_ins_table_insert = ("""INSERT INTO transfer_ins_table
                        (
                            id,
                            account_id,
                            amount,
                            transaction_requested_at,
                            transaction_completed_at,
                            status
                        )
                        VALUES (%s, %s,%s, %s,%s, %s);"""
                    )

transfer_outs_table_insert = ("""INSERT INTO transfer_outs_table
                        (
                            id,
                            account_id,
                            amount,
                            transaction_requested_at,
                            transaction_completed_at,
                            status
                        )
                        VALUES (%s, %s, %s, %s,%s, %s);"""
                    )

state_table_insert = ("""INSERT INTO state_table
                        (
                            state_id,
                            state,
                            country_id
                        )
                        VALUES (%s, %s, %s);"""
                    )

fact_movements_table_insert = ("""INSERT INTO fact_movements_table
                        (
                            id,
                            account_id,
                            customer_id,
                            in_or_out,
                            type,
                            amount,
                            requested_at,
                            completed_at,
                            status
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
                    )
                     
dim_time_table_insert = ("""CREATE TABLE IF NOT EXISTS dim_time_table
                        (
                            time_id,
                            action_timestamp,
                            action_week,
                            action_month,
                            action_year,
                            action_weekday
                        )
                        VALUES (%s, %s, %s, %s, %s, %s);"""
                    )
                     
dim_customers_table_insert = ("""INSERT INTO customers_table
                        (
                        customer_id,
                        first_name,
                        last_name,
                        city,
                        state,
                        country,
                        cpf
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (customer_id) DO NOTHING;"""
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

create_table_queries = [
                            accounts_table_create,
                            city_table_create,
                            customers_table_create,
                            country_table_create,
                            d_month_table_create,
                            d_time_table_create,
                            d_week_table_create,
                            d_weekday_table_create,
                            d_year_table_create,
                            pix_movements_table_create,
                            state_table_create,
                            transfer_ins_table_create,
                            transfer_outs_table_create,
                            fact_movements_table_create,
                            dim_time_table_create,
                            dim_customers_table_create
                        ]

drop_table_queries = [
                            accounts_table_drop,
                            city_table_drop,
                            customers_table_drop,
                            country_table_drop,
                            d_month_table_drop,
                            d_time_table_drop,
                            d_week_table_drop,
                            d_weekday_table_drop,
                            d_year_table_drop,
                            pix_movements_table_drop,
                            state_table_drop,
                            transfer_ins_table_drop,
                            transfer_outs_table_drop,
                            fact_movements_table_drop,
                            dim_time_table_drop,
                            dim_customers_table_drop
                    ]