generic
   type T_Donnee is private;
package Naive is
   type Table_Naive is array (Positive range <>, Positive range <>) of T_Donnee;
end Naive;
