<?php

class pageView
{

    public function __construct()
    {

        //ビューID
        $viewId = 117048127;

        //GoogleAPI クライアント メールアドレス
        $client_email = 'mu.mizutani@gmail.com';

        //.p12ファイル(秘密鍵)
        $private_key = file_get_contents(P12KEY);
    }

    public function getPageView()
    {
        //メトリクス:取得するデータ ga:pageviewsはPV数
        $metrics = "ga:pageviews";

        //取得期間(Y-m-d形式)
        $from = '2015-08-10';
        $to = '2015-08-12';

        //オプション
        $option = [
            "dimensions" => 'ga:date', //ディメンション:区切り 日付ごとに
            "max-results" => 10000, //最大取得件数 10000がAPIの上限
            "sort" => "ga:date", //ソート 日付順
        ];


        //スコープのセット
        $scopes = ["https://www.googleapis.com/auth/analytics.readonly"];

        //クレデンシャルの作成
        $credentials = new Google_Auth_AssertionCredentials($client_email, $scopes, $private_key);

        //Googleクライアントのインスタンスを作成
        $client = new Google_Client();
        $client->setAssertionCredentials($credentials);

        //トークンのリフレッシュ
        if ($client->getAuth()->isAccessTokenExpired()) {
            $client->getAuth()->refreshTokenWithAssertion($credentials);
        }
        $_SESSION["service_token"] = $client->getAccessToken();

        //Analyticsのインスタンスを作成
        $analytics = new Google_Service_Analytics($client);

        //データの取得
        $obj = $analytics->data_ga->get(
            "ga:{$viewId}",
            $from,
            $to,
            $metrics,
            $option
        );

        echo '<pre>';
        var_dump($obj->rows);
        echo '</pre>';
    }

}
