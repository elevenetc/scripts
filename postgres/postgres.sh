alias pg-start="brew services start postgresql"
alias pg-kill="brew services stop postgresql"
alias pg-check-port="egrep 'listen|port' /usr/local/var/postgres/postgresql.conf"
alias pg-status="pg_ctl -D /usr/local/var/postgres status"
alias pg-connect="psql -U postgres"
alias pg-list-databases="psql -U postgres -l"
