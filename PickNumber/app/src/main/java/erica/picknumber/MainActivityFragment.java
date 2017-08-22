package erica.picknumber;

import android.content.Context;
import android.support.v4.app.Fragment;
import android.os.Bundle;
import android.support.v4.app.FragmentTransaction;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.InputMethodManager;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;


import butterknife.BindView;
import butterknife.ButterKnife;


/**
 * A simple {@link Fragment} subclass.
 * Activities that contain this fragment must implement the
 * {@link MainActivityFragment.OnFragmentInteractionListener} interface
 * to handle interaction events.
 * Use the {@link MainActivityFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class MainActivityFragment extends Fragment {
    @BindView(R.id.pickNumberButton) Button pickNumberButton;
    @BindView(R.id.nameField) AutoCompleteTextView nameField;
    @BindView(R.id.viewTableButton) Button viewTableButton;

    public MainActivityFragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
      final View v = inflater.inflate(R.layout.fragment_main_activity, container, false);
      final Context context = getContext();
      final MainActivity main = (MainActivity) getActivity();
      ButterKnife.bind(this, v);

      ArrayAdapter<String> adapter = new ArrayAdapter<String>(context,
              android.R.layout.simple_selectable_list_item, COUNTRIES);
      nameField.setAdapter(adapter);
      nameField.setOnItemClickListener(new AdapterView.OnItemClickListener() {
          @Override
          public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
              InputMethodManager imm = (InputMethodManager) context.getSystemService(context.INPUT_METHOD_SERVICE);
              imm.hideSoftInputFromWindow(v.getWindowToken(), 0);
          }
      });

      viewTableButton.setOnClickListener(new View.OnClickListener() {
          @Override
          public void onClick(View v) {
            // Switch from MainActivityFragment to AdminFragment.
            Fragment adminFragment = new AdminFragment();
            main.replaceFragment(adminFragment);
          }
      });

      pickNumberButton.setOnClickListener(new View.OnClickListener() {
          @Override
          public void onClick(View view) {
            Fragment numFragment = new NumberFragment();
            main.replaceFragment(numFragment);
          }
      });
      return v;
    }

    private static final String[] COUNTRIES = new String[] {
            "Frank Bellbottom", "Francis Fiasco", "Fringe Fuller", "Fiana Fior", "Fuloco Fascisca"
    };

}
