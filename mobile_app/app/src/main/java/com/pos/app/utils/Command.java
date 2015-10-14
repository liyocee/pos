package com.pos.app.utils;

import android.app.ProgressDialog;
import org.json.JSONObject;

public interface Command {
    ProgressDialog doPreExecute();

    void handleHttpError();

    void handleHttpSuccess(JSONObject jObj);

    String getAuthToken();
}
