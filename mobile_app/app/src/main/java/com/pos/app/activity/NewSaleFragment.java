package com.pos.app.activity;
import android.os.Bundle;
import android.util.Log;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Button;

import com.pos.app.R;


public class NewSaleFragment extends Fragment {
    private static final String ARG_SECTION_NUMBER = "section_number";


    public static NewSaleFragment newInstance(int sectionNumber) {
        NewSaleFragment fragment = new NewSaleFragment();
        Bundle args = new Bundle();
        args.putInt(ARG_SECTION_NUMBER, sectionNumber);
        fragment.setArguments(args);
        return fragment;
    }

    public NewSaleFragment() {
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
        return rootView;
    }

}
