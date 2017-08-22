package erica.picknumber;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import butterknife.BindView;
import butterknife.ButterKnife;


/**
 * This fragment is password protected. On this fragment, the admin can view and clear the database
 * and set the capacity.
 */
public class AdminFragment extends Fragment {
  @BindView(R.id.adminDoneButton) Button adminDoneButton;
  @BindView(R.id.capacityNumberField) EditText capacityNumberField;
  @BindView(R.id.dropTableButton) Button dropTableButton;

  public AdminFragment() {
  }

  @Override
  public View onCreateView(LayoutInflater inflater, ViewGroup container,
                           Bundle savedInstanceState) {
    View v = inflater.inflate(R.layout.fragment_admin, container, false);
    ButterKnife.bind(this, v);

    final MainActivity main = (MainActivity) getActivity();

    capacityNumberField.se

    adminDoneButton.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View view) {
          Fragment fragment = new MainActivityFragment();
          main.replaceFragment(fragment);
        }
    });

      return v;
  }


}
