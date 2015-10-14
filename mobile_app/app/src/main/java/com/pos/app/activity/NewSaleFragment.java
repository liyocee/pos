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
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Button;
import android.widget.Toast;
import com.pos.app.Constants;
import com.pos.app.R;
import com.pos.app.pojos.Product;
import com.pos.app.utils.Command;
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
        View rootView = inflater.inflate(R.layout.fragment_new_sale, container, false);
//        TextView textView = (TextView) rootView.findViewById(R.id.product);
//        textView.setText(getString(R.string.section_format, getArguments().getInt(ARG_SECTION_NUMBER)));
        Button btn = (Button) rootView.findViewById(R.id.saveSaleButton);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.e("Clicked", "about to save");
            }
        });
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
