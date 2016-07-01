package app;

import ratpack.func.Action;

public class Helpers {
  public static <T> Action<T> act(Func<T> func) {
    return Action.from(func::func);
  }
}
