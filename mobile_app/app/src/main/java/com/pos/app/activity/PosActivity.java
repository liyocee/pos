package com.pos.app.activity;

import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.design.widget.TabLayout;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.support.v4.view.ViewPager;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Toast;

import com.pos.app.Constants;
import com.pos.app.R;
import com.pos.app.utils.Command;
import com.pos.app.utils.HttpAsync;
import org.json.JSONObject;

public class PosActivity extends AppCompatActivity implements Command{

    private SectionsPagerAdapter mSectionsPagerAdapter;
    private SharedPreferences mPreferences;

    private ViewPager mViewPager;
    private Context context;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pos);
        context = this;
        mPreferences = getSharedPreferences(Constants.USER_DATA, MODE_PRIVATE);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        // Create the adapter that will return a fragment for each of the three
        // primary sections of the activity.
        mSectionsPagerAdapter = new SectionsPagerAdapter(getSupportFragmentManager());

        // Set up the ViewPager with the sections adapter.
        mViewPager = (ViewPager) findViewById(R.id.container);
        mViewPager.setAdapter(mSectionsPagerAdapter);

        TabLayout tabLayout = (TabLayout) findViewById(R.id.tabs);
        tabLayout.setupWithViewPager(mViewPager);

    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_pos, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        JSONObject myParams = new JSONObject();
        if (id == R.id.logout) {
            new HttpAsync(context, this, Constants.LOGOUT_URL, myParams).execute();
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
    public ProgressDialog doPreExecute(){
        Log.v("Singing out", "Please Wait....");
        return ProgressDialog.show(PosActivity.this, "Signing out", "Please Wait...", true);
    }

    public void handleHttpError(){
        Toast.makeText(context, "Error signing out",
                Toast.LENGTH_LONG).show();
    }

    public void handleHttpSuccess(JSONObject jObj){
        SharedPreferences.Editor editor = mPreferences.edit();
        try{

            editor.remove("token");
            editor.remove("organization");
            editor.remove("agent_id");
            editor.remove("agent_name");
            editor.commit();
            Toast.makeText(context, "Successfully signed out",
                    Toast.LENGTH_LONG).show();
            Intent intent = new Intent(context, WelcomeActivity.class);
            context.startActivity(intent);
        }catch(Exception e){
            e.printStackTrace();
        }


    }
    public class SectionsPagerAdapter extends FragmentPagerAdapter {

        public SectionsPagerAdapter(FragmentManager fm) {
            super(fm);
        }

        @Override
        public Fragment getItem(int position) {
            Fragment frag = null;
            switch(position){
                case 0:
                    frag = NewSaleFragment.newInstance(position + 1);
                    break;
                case 1:
                    frag = SalesListFragment.newInstance(position + 1);
                    break;
            }
            return frag;
        }

        @Override
        public int getCount() {
            return 2;
        }

        @Override
        public CharSequence getPageTitle(int position) {
            switch (position) {
                case 0:
                    return "Add Sale";
                case 1:
                    return "My Sales";
            }
            return null;
        }
    }

}
