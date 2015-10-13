#!/usr/bin/env bash
source /root/.virtualenvs/pos/bin/activate
export DB_NAME="pos_db"
export DB_USER="pos_user"
export DB_PASS="pos_passwd"
export STATIC_ROOT="/opt/pos/static/"
export MEDIA_ROOT="/opt/pos/media/"
export MEDIA_URL='http://pos.healthix.co.ke/media/'
export CSRF_COOKIE_DOMAIN=".healthix.co.ke"
export SESSION_COOKIE_DOMAIN=".healthix.co.ke"
export SECRET_KEY="s*n$9t9no43118w$y603)@=(**$0b$cj_kzpe@t(we!6a&(#s+"
export CLIENT_ORIGIN="pos.co.ke"
export DJANGO_SETTINGS_MODULE="config.production"
export DEBUG="false"