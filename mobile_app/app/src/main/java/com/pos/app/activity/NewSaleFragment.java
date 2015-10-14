package com.pos.app.activity;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Button;
import android.widget.Toast;
import com.pos.app.Constants;
import com.pos.app.R;
import com.pos.app.pojos.Product;
import com.pos.app.utils.Command;
import com.pos.app.utils.CreateSaleAsync;
import com.pos.app.utils.GPSManager;
import com.pos.app.utils.HttpAsync;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class NewSaleFragment extends Fragment implements Command {
    private static final String ARG_SECTION_NUMBER = "section_number";
    private SharedPreferences mPreferences = null;
    private static Context context = null;
    private static int MODE_PRIVATE;
    JSONArray productsArray;
    ArrayList<String> productsList = new ArrayList<String>();
    ArrayList<Product> products = new ArrayList<Product>();
    View view = null;
    GPSManager gpsTracker = null;

    public static NewSaleFragment newInstance(int sectionNumber, int preferencesMode) {
        NewSaleFragment fragment = new NewSaleFragment();
        Bundle args = new Bundle();
        args.putInt(ARG_SECTION_NUMBER, sectionNumber);
        fragment.setArguments(args);
        context = fragment.getContext();
        MODE_PRIVATE = preferencesMode;
        return fragment;

    }

    public NewSaleFragment() {
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        context = this.getContext();
        gpsTracker = new GPSManager(context);
        mPreferences = context.getSharedPreferences(Constants.USER_DATA, NewSaleFragment.MODE_PRIVATE);
        JSONObject myParams = new JSONObject();
        String url = Constants.PRODUCTS_URL+mPreferences.getString("organization", "");
        url = url+"&page_size=1000";
        new HttpAsync(context, this, url,"GET", myParams).execute();
    }
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        final View rootView = inflater.inflate(R.layout.fragment_new_sale, container, false);
        Button btn = (Button) rootView.findViewById(R.id.saveSaleButton);
        TextView textLatitude = (TextView)rootView.findViewById(R.id.latitude);
        TextView textLongitude = (TextView)rootView.findViewById(R.id.longitude);
        if(gpsTracker.canGetLocation()){
            // set latitude
            String stringLatitude = String.valueOf(gpsTracker.getLatitude());
            textLatitude.setText(stringLatitude);
            String stringLongitude = String.valueOf(gpsTracker.getLongitude());
            textLongitude.setText(stringLongitude);
        }else{
            textLatitude.setText("");
            textLongitude.setText("");
        }
        this.view = rootView;

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                TextView latitudeField = (TextView) rootView.findViewById(R.id.latitude);
                String mLatitude = latitudeField.getText().toString();
                TextView longitudeField = (TextView) rootView.findViewById(R.id.longitude);
                String mLongitude = longitudeField.getText().toString();
                TextView emailField = (TextView) rootView.findViewById(R.id.customerEmail);
                String mEmail = emailField.getText().toString();
                TextView phoneField = (TextView) rootView.findViewById(R.id.customerPhone);
                String mPhone = phoneField.getText().toString();
                TextView idNumberField = (TextView) rootView.findViewById(R.id.customerPhone);
                String mIdNumber = idNumberField.getText().toString();
                TextView firstNameField = (TextView)rootView.findViewById(R.id.customerFirstName);
                String mFirstName = firstNameField.getText().toString();
                TextView lastNameField = (TextView)rootView.findViewById(R.id.customerLastName);
                String mLastName = lastNameField.getText().toString();
                TextView productField = (TextView)rootView.findViewById(R.id.product_id);
                String mProductId = productField.getText().toString();
                String mFollowUpDate = "2015-10-16T10:04:00";
                String mAgent = mPreferences.getString("agent_id", "");

                try{
                    JSONObject prod = new JSONObject();
                    prod.put("latitude", mLatitude);
                    prod.put("longitude", mLongitude);
                    prod.put("product", mProductId);
                    prod.put("agent", mAgent);
                    prod.put("customer_email", mEmail);
                    prod.put("customer_phone", mPhone);
                    prod.put("customer_first_name", mFirstName);
                    prod.put("customer_last_name", mLastName);
                    prod.put("customer_id_number", mIdNumber);
                    prod.put("follow_up_date", mFollowUpDate);

                    Log.e("CREATE_PROD", prod.toString());
                    CreateSaleAsync saleAsync = new CreateSaleAsync(context, mPreferences, rootView);
                    new HttpAsync(context, saleAsync, Constants.SALES_URL, "POST", prod).execute();
                }catch(JSONException e){
                    e.printStackTrace();
                }

            }
        });
        return rootView;
    }

    public ProgressDialog doPreExecute(){
        Log.v("Singing out", "Please Wait....");
        return ProgressDialog.show(NewSaleFragment.context, "Fetching Products", "Please Wait...", true);
    }
    public void handleHttpError(){
        Toast.makeText(context, "Error connecting to server",
                Toast.LENGTH_LONG).show();
    }

    public void handleHttpSuccess(JSONObject jObj){
        try{
            productsArray = jObj.getJSONArray("results");
            for(int i=0; i<productsArray.length(); i++){
                JSONObject prod = productsArray.getJSONObject(i);
                Product product = new Product();
                product.setId(prod.getString("id"));
                product.setName(prod.getString("name"));
                products.add(product);
                // populate product names
                productsList.add(prod.getString("name"));

                Log.e("PRODUCT", productsList.toString());
            }
            Spinner mySpinner = (Spinner) view.findViewById(R.id.product);
            ArrayAdapter<String> adapter = new ArrayAdapter<String>(
                    getActivity(),
                    android.R.layout.simple_spinner_item,
                    productsList
            );
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
            mySpinner.setAdapter(adapter);
            mySpinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {

                @Override
                public void onItemSelected(AdapterView<?> arg0,
                                           View arg1, int position, long arg3) {
                    TextView txtProductId = (TextView) view.findViewById(R.id.product_id);
                    // Set the text followed by the position
                        txtProductId.setText(products.get(position).getId());
                }

                @Override
                public void onNothingSelected(AdapterView<?> arg0) {
                }
            });
            Toast.makeText(context, "Successfully fetched the products",
                    Toast.LENGTH_LONG).show();
        }catch(JSONException e){
            e.printStackTrace();
        }
    }
    public String getAuthToken(){
        return mPreferences.getString("token", "");
    }

}
