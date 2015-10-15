package com.pos.app.activity;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v4.app.ListFragment;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Toast;

import com.pos.app.Constants;
import com.pos.app.pojos.Sale;
import com.pos.app.utils.Command;
import com.pos.app.utils.HttpAsync;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class SalesListFragment extends ListFragment implements Command {

    private static final String ARG_SECTION_NUMBER = "section_number";
    private SharedPreferences mPreferences = null;
    private static Context context = null;
    private static int MODE_PRIVATE;
    JSONArray salesArray;
    ArrayList<String> salesList = null;
    ArrayList<Sale> sales = null;
    View view = null;

    public static SalesListFragment newInstance(int sectionNumber, int preferenceMode) {
        SalesListFragment fragment = new SalesListFragment();
        Bundle args = new Bundle();
        args.putInt(ARG_SECTION_NUMBER, sectionNumber);
        fragment.setArguments(args);
        MODE_PRIVATE = preferenceMode;
        Log.e("FRAG_LOG 1", "here");
        return fragment;
    }
    public SalesListFragment() {
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        context = this.getContext();
        mPreferences = context.getSharedPreferences(Constants.USER_DATA, SalesListFragment.MODE_PRIVATE);
        fetchSales();
    }

    @Override
    public void onResume(){
        super.onResume();
        fetchSales();
    }

    @Override
    public void onStart(){
        super.onStart();
        fetchSales();
    }

    private void fetchSales(){
        JSONObject myParams = new JSONObject();
        String url = Constants.SALES_URL+"?agent="+mPreferences.getString("agent_id", "");
        url = url+"&page_size=1000";
        new HttpAsync(context, this, url,"GET", myParams).execute();
    }
    public ProgressDialog doPreExecute(){
        return ProgressDialog.show(SalesListFragment.context, "Fetching Sales", "Please Wait...", true);
    }
    public void handleHttpError(){
        Toast.makeText(context, "Error connecting to server",
                Toast.LENGTH_LONG).show();
    }

    public void handleHttpSuccess(JSONObject jObj){
        salesList = new ArrayList<String>();
        sales = new ArrayList<Sale>();
        try{
            salesArray = jObj.getJSONArray("results");
            Log.e("SALE_ARRAY", salesArray.toString());
            for(int i=0; i<salesArray.length(); i++){
                JSONObject sale = salesArray.getJSONObject(i);
                Sale saleItem = new Sale();
                saleItem.setLatitude(sale.getString("latitude"));
                saleItem.setLongitude(sale.getString("longitude"));
                saleItem.setCustomerEmail(sale.getString("customer_email"));
                saleItem.setCustomerFirstName(sale.getString("customer_first_name"));
                saleItem.setCustomerLastName(sale.getString("customer_last_name"));
                saleItem.setCustomerPhone(sale.getString("customer_phone"));
                saleItem.setCustomerIdNumber(sale.getString("customer_id_number"));
                JSONObject prod = sale.getJSONObject("product_details");
                saleItem.setProduct(prod.getString("name"));
                sales.add(saleItem);
                // populate sales names
                String customerName = sale.getString("customer_first_name")+" "+sale.getString("customer_last_name");
                salesList.add(prod.getString("name") + " , sold to  " + customerName);
            }
            Log.e("HAPA", salesList.toString());
            setListAdapter(new ArrayAdapter<String>(
                    getActivity(),
                    android.R.layout.simple_list_item_1,
                    salesList));

            Toast.makeText(context, "Successfully fetched my sales",
                    Toast.LENGTH_LONG).show();
        }catch(JSONException e){
            e.printStackTrace();
        }
    }
    public String getAuthToken(){
        return mPreferences.getString("token", "");
    }
}
