package com.pos.app.activity;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;
import org.json.JSONException;
import org.json.JSONObject;
import com.pos.app.R;
import com.pos.app.utils.Command;
import com.pos.app.utils.HttpAsync;

public class LoginActivity extends AppCompatActivity implements Command {
    private SharedPreferences mPreferences;
    Context context;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        context = this;
        mPreferences = getSharedPreferences("CurrentUser", MODE_PRIVATE);
    }

    public void userLogin(View button) {
        EditText userNameField = (EditText) findViewById(R.id.userEmail);
        String mUserName = userNameField.getText().toString();
        EditText userPasswordField = (EditText) findViewById(R.id.userPassword);
        String mUserPassword = userPasswordField.getText().toString();
        try{
            JSONObject myParams = new JSONObject();
            myParams.put("username", mUserName);
            myParams.put("password", mUserPassword);
            Log.d("Register User Params", myParams.toString() + "");
            new HttpAsync(context, this, myParams).execute();
        }catch(JSONException e){
            e.printStackTrace();
        }

    }

    public ProgressDialog doPreExecute(){
        Log.v("Singing", "Please Wait....");
        return ProgressDialog.show(LoginActivity.this, "Signing in", "Please Wait...", true);
    }

    public void handleHttpError(){
        Toast.makeText(context, "Invalid Username/Password",
                Toast.LENGTH_LONG).show();
    }

    public void handleHttpSuccess(JSONObject jObj){
        SharedPreferences.Editor editor = mPreferences.edit();
        try{
            editor.putString("token", jObj.getString("key"));
            JSONObject user = jObj.getJSONObject("user");
            JSONObject org = user.getJSONObject("organization");
            JSONObject agent = user.getJSONObject("agent");
            editor.putString("organization", org.getString("id"));
            editor.putString("agent_id", agent.getString("id"));
            editor.putString("agent_name", user.getString("full_name"));
            editor.commit();
            Toast.makeText(context, "Welcome " + user.getString("full_name") + "",
                    Toast.LENGTH_LONG).show();
            Intent intent = new Intent(context, PosActivity.class);
            context.startActivity(intent);
        }catch(JSONException e){
            e.printStackTrace();
        }

    }


}