private String formatSqlParamater(String sqlParamater){
        String paramater = "";
        switch (sqlParamater){
            case "int":
                paramater = "Integer";
                break;
            case "bigint":
                paramater = "Long";
                break;
            case "varchar":
                paramater = "String";
                break;
            case "datetime":
                paramater = "Date";
                break;
            case "timestamp":
                paramater = "Date";
                break;
        }
        return paramater;
    }
