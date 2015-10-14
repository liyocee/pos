package com.pos.app.utils;

import android.app.ProgressDialog;
import android.content.Context;
import android.content.SharedPreferences;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.pos.app.R;

import org.json.JSONObject;

public class CreateSaleAsync implements Command{
    Context context = null;
    SharedPreferences mPreferences = null;
    View rootView = null;
    public CreateSaleAsync(Context context, SharedPreferences mPreferences, View v){
        this.context = context;
        this.mPreferences = mPreferences;
        this.rootView = v;
    }

    public ProgressDialog doPreExecute(){
        return ProgressDialog.show(this.context, "Creating Sale", "Please Wait...", true);
    }
    public void handleHttpError(){
        Toast.makeText(context, "Error saving the sale details",
                Toast.LENGTH_LONG).show();
    }

    public void handleHttpSuccess(JSONObject jObj){
        ((TextView)rootView.findViewById(R.id.customerEmail)).setText("");
        ((TextView)rootView.findViewById(R.id.customerPhone)).setText("");
        ((TextView)rootView.findViewById(R.id.customerPhone)).setText("");
        ((TextView)rootView.findViewById(R.id.customerFirstName)).setText("");
        ((TextView)rootView.findViewById(R.id.customerLastName)).setText("");
        ((TextView)rootView.findViewById(R.id.customerIdNumber)).setText("");
        ((TextView)rootView.findViewById(R.id.product_id)).setText("");
        try{

            Toast.makeText(context, "Successfully saved the sale",
                    Toast.LENGTH_LONG).show();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    public String getAuthToken(){
        return mPreferences.getString("token", "");
    }
}
