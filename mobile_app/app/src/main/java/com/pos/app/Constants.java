package com.pos.app;

public class Constants {

    public static final String SERVER_BASE_URL = "http://pos-api.healthix.co.ke/api/v1/";
    public static final String LOGIN_URL = SERVER_BASE_URL+"auth/login/";
    public static final String LOGOUT_URL = SERVER_BASE_URL+"auth/logout/";
    public static final String SALES_URL = SERVER_BASE_URL+"pos/sales/";
    public static final String PRODUCTS_URL = SERVER_BASE_URL+"pos/product_types/?organization=";
    public static final String USER_DATA = "CurrentUser";
    private Constants() {
    }

}
