package com.pos.app.activity;
import android.os.Bundle;
import android.support.v4.app.ListFragment;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import com.pos.app.activity.dummy.DummyContent;
public class SalesListFragment extends ListFragment {

    private static final String ARG_SECTION_NUMBER = "section_number";
    private  String mParam1;
    private static int MODE_PRIVATE;

    public static SalesListFragment newInstance(int sectionNumber, int preferenceMode) {
        SalesListFragment fragment = new SalesListFragment();
        MODE_PRIVATE = preferenceMode;
        Bundle args = new Bundle();
        args.putInt(ARG_SECTION_NUMBER, sectionNumber);
        fragment.setArguments(args);
        return fragment;
    }
    public SalesListFragment() {
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_SECTION_NUMBER);
        }

        // TODO: Change Adapter to display your content
        setListAdapter(new ArrayAdapter<DummyContent.DummyItem>(getActivity(),
                android.R.layout.simple_list_item_1, android.R.id.text1, DummyContent.ITEMS));
    }

    @Override
    public void onListItemClick(ListView l, View v, int position, long id) {
        super.onListItemClick(l, v, position, id);
    }
}
