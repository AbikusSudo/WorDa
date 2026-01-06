package io.abikussudo.sagernet.bg.proto

import io.abikussudo.sagernet.database.DataStore
import io.abikussudo.sagernet.database.ProxyEntity

class UrlTest {

    val link = DataStore.connectionTestURL
    private val timeout = 5000

    suspend fun doTest(profile: ProxyEntity): Int {
        return TestInstance(profile, link, timeout).doTest()
    }

}