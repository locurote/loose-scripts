
dbus_name=''
dbus_path=''

main() {
    proces_args $@

    if [[ -n $dbus_name ]]
    then

        if [[ -z $dbus_path ]]
        then
            dbus_path='/'${dbus_name//.//}
            # dbus_path=${dbus_path,,}         
        fi
        
        echo -e "\"$dbus_name\",\n\"$dbus_path\""

        dbus-send --session \
            --type=method_call \
            --dest=$dbus_name \
            --print-reply \
            $dbus_path \
            org.freedesktop.DBus.Introspectable.Introspect
    fi
}

help() {
    echo "Usage:
-p, --path [path]        path of the interface
-n, --name [name]        name of the interface
-h                       opens this menu
"
}

assert_not_empty() {
    if [[ -z $1 ]]
    then
        echo "[err] argument has no value"
        help
        exit 1 
    fi
}

proces_args() {
    args=("$@")

    if [[ $# == 0 ]]
    then
        echo "[err] no arguments provided"
        help
        exit 1
    fi

    for ((i = 0 ; i < ${#args[@]} ; i++))
    do
        arg=${args[$i]}
        argv=${args[$((i + 1))]}

        case $arg in
            --name | -n)
                assert_not_empty $argv
                dbus_name=$argv
                ((i++))
            ;;
            --path | -p)
                assert_not_empty $argv
                dbus_path=$argv
                ((i++))
            ;;
            --help | -h)
                help
            ;;   
            *)
                help
            ;;
        esac
    done
}

# main call
main $@