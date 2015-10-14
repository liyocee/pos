package com.pos.app.activity;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import com.pos.app.R;
public class WelcomeActivity extends AppCompatActivity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_welcome_login);
        findViewById(R.id.loginButton).setOnClickListener(
            new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    // Existing Account, load login view
                    Intent intent = new Intent(WelcomeActivity.this,
                            LoginActivity.class);
                    startActivityForResult(intent, 0);
                }
            });

    }

    @Override
    public void onBackPressed() {
        Intent startMain = new Intent(Intent.ACTION_MAIN);
        startMain.addCategory(Intent.CATEGORY_HOME);
        startMain.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        startActivity(startMain);
        finish();
    }

    @Override
    protected void onResume() {
        super.onResume();
    }
}
