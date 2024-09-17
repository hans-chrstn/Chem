{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  nativeBuildInputs = with pkgs; [
    (python3.withPackages(ps: with ps; [
      pip
      pyqt6
    ])) 
    qt6.full
  ];
  shellHook = ''
    export QT_QPA_PLATFORM=wayland
  '';

}
