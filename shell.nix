{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "mlops-env";

  packages = with pkgs; [
    python313
    stdenv.cc.cc.lib  # libstdc++.so.6 for numpy
    zlib              # compress lib
    glib              # system lib
    
    git               #these two for data pipelining
    dvc

  ];

  #shout out :D
  shellHook = ''
    export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:$LD_LIBRARY_PATH
    echo "MLops on Nix-shell!!"
    exec zsh
  '';
}
