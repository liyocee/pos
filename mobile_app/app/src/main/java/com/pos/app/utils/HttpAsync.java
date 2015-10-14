package com.pos.app.utils;
import android.app.ProgressDialog;
import android.os.AsyncTask;
import android.util.Log;
import android.content.Context;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.StatusLine;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;

public class HttpAsync extends AsyncTask<String, String, Void> {
    JSONObject jObj = null;
    JSONObject myParams = null;
    String json = "";
    String url = "";
    ProgressDialog progress = null;
    int statusCode;
    protected Context context = null;
    protected Command command = null;
    public HttpAsync(Context currentContext,Command command, String url, JSONObject params){
        this.context = currentContext;
        this.myParams = params;
        this.command = command;
        this.url = url;
    }

    @Override
    protected void onPreExecute() {
        command.doPreExecute();
        super.onPreExecute();
    }

    @Override
    protected Void doInBackground(String... params) {
        InputStream mis = null;
        // Making HTTP request
        try {
            // defaultHttpClient
            HttpClient httpClient = new DefaultHttpClient();
            HttpPost httpPost = new HttpPost(this.url);
            StringEntity stringEntity = new StringEntity(myParams.toString());
            stringEntity.setContentEncoding("UTF-8");
            stringEntity.setContentType("application/json");
            httpPost.setEntity(stringEntity);
            httpPost.setHeader("Accept", "application/json");
            httpPost.setHeader("Content-Type", "application/json");

            HttpResponse httpResponse = httpClient.execute(httpPost);
            HttpEntity httpEntity = httpResponse.getEntity();
            mis = httpEntity.getContent();
            StatusLine statusLine = httpResponse.getStatusLine();
            statusCode = statusLine.getStatusCode();
            Log.e("HTTP STATUS ", statusLine.getReasonPhrase());
            Log.e("HTTP STATUS ", statusLine.toString());

            BufferedReader reader = new BufferedReader(new InputStreamReader(
                    mis, "iso-8859-1"), 8);
            StringBuilder sb = new StringBuilder();
            String line = null;
            while ((line = reader.readLine()) != null) {
                sb.append(line + "n");
            }
            mis.close();
            json = sb.toString();
            Log.e("JSON", json);
            // try parse the string to a JSON object
            jObj = new JSONObject(json);
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
            statusCode = 0;
        } catch (ClientProtocolException e) {
            e.printStackTrace();
            progress.dismiss();
        } catch (IOException e) {
            e.printStackTrace();
            statusCode = 0;
            progress.dismiss();
        } catch (Exception e) {
            statusCode = 0;
            progress.dismiss();
            Log.e("Buffer Error", "Error converting result " + e.toString());
        }
        return null;
    }

    @Override
    protected void onPostExecute(Void aVoid) {
        Log.e("JSONObject", "" + String.valueOf(json));
        try {
            if(statusCode >= 400){
                command.handleHttpError();
            }else {
                command.handleHttpSuccess(jObj);
            }
            progress.dismiss();

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            super.onPostExecute(aVoid);
        }
    }
}