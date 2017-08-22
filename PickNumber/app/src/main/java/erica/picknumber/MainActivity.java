package erica.picknumber;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

  private int capacity;

  @Override
  public void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);

      Fragment fragment = new MainActivityFragment();
      FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
      transaction.add(R.id.fragment_container, fragment, "MainActivityFragment");
      transaction.commit();
  }

  public int getCapacity() {
    return capacity;
  }

  public void setCapacity(int capacity) {
    this.capacity = capacity;
  }

  /**method replaces the current fragment with the fragment
   that is given as an input */
  public void replaceFragment(Fragment fragment) {
      FragmentManager manager;                                            //initializes manager as FragmentManager
      FragmentTransaction transaction;                                    //initializes transaction as FragmentTransaction
      manager = getSupportFragmentManager();
      transaction = manager.beginTransaction();
      transaction.replace(R.id.fragment_container, fragment);
      transaction.addToBackStack(null).commit();
  }
}
