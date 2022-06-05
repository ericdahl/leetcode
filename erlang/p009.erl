-spec is_palindrome(X :: integer()) -> boolean().
is_palindrome(X) ->
  integer_to_list(X) == lists:reverse(integer_to_list(X)).