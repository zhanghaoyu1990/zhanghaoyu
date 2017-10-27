package com.pingan.jkkit.fs.other.contract.common.util;

import java.security.MessageDigest;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.TreeMap;

import org.apache.log4j.Logger;


/** 
 * @author 作者 陈强 <br>
 * @version 创建时间：2015年11月6日 下午9:55:13 <br>
 * <h1>类说明</h1>
 */
public class NoticeMD5Security{
	private static String ecoding = "UTF-8";
	public static final String SECRET = "insurance.jiankangka";
	private static Logger			logger	= Logger.getLogger(NoticeMD5Security.class);

	public static void md5(Map<String, String> pramap,String secret) throws Exception {
		String result = null;
		String msg = "";
		if(pramap != null)
			msg = coverMap2String(pramap);
		msg = msg + "&key=" + secret;
		try
		{
			MessageDigest md = MessageDigest.getInstance("MD5");
			result = byte2hex(md.digest(msg.getBytes(ecoding)));
			pramap.put("sign", result);
		}catch(Exception e)
		{
			throw new RuntimeException("签名失败：", e);
		}
		//return result;
	}
	
	private static String byte2hex(byte[] b)
	{
		StringBuffer hs = new StringBuffer();
		String stmp = "";
		for(int n = 0;n < b.length;++n)
		{
			stmp = Integer.toHexString(b[n] & 0xFF);
			if(stmp.length() == 1)
				hs.append("0").append(stmp);
			else
				hs.append(stmp);
		}
		return hs.toString().toLowerCase();
	}
	
	/**
	 * 对map里面的键值对数据，按key进行排序，并按key=value&key1=value1的组装方式返回string
	 * @param data Map<String,String>
	 * @return String
	 * @throws Exception
	 */
	@SuppressWarnings({ "rawtypes", "unchecked" })
	public static String coverMap2String(Map<String, String> data) throws Exception{
		String resString = "";
		TreeMap tree = new TreeMap();
		Iterator it = data.entrySet().iterator();
		while (it.hasNext()) {
			Map.Entry en = (Map.Entry) it.next();
			if ("sign".equals(((String) en.getKey()).trim())||en.getKey()==null) {
				continue;
			}
			tree.put(en.getKey(), en.getValue());
		}
		it = tree.entrySet().iterator();
		StringBuffer sf = new StringBuffer();
		while (it.hasNext()) {
			Map.Entry en = (Map.Entry) it.next();
			sf.append(new StringBuilder().append((String) en.getKey()).append("=").append((String) en.getValue()).append("&").toString());
		}
		if(sf.length()>1)
			resString = sf.substring(0, sf.length() - 1);
		return resString;
	}
	
	/**
	 * 验证md5签名
	 * @param pramap
	 * @param secret
	 * @throws Exception
	 */
	public static boolean validatemd5(Map<String, String> pramap,String secret,String sign) throws Exception {
		boolean bool = false;
		logger.info("validatemd5签名sign："+sign);
		String msg = "";
		if(pramap != null)
			msg = coverMap2String(pramap);
		logger.info("validatemd5签名msg："+msg);
		msg = msg + "&key=" + secret;
		try
		{
			MessageDigest md = MessageDigest.getInstance("MD5");
			String result = byte2hex(md.digest(msg.getBytes(ecoding)));
			logger.info("validatemd5签名result："+result);
			if(sign.equals(result)){
				bool = true; 
			}
		}catch(Exception e)
		{
			throw new RuntimeException("验证签名失败：", e);
		}
		return bool;
	}
	
    public static void main(String[] args) {
		String secret = NoticeMD5Security.SECRET;
		Map<String, String> pramap = new HashMap<String,String>();
		pramap.put("format","1" );
		pramap.put("from","2" );
		pramap.put("payOrderNo","3" );
		pramap.put("payStatus","4" );
		pramap.put("pamaAcct","5" );
		pramap.put("channelOrderNo","6" );
		pramap.put("pamaChannelId","7" );
		pramap.put("payTime","8" );
		//加签
		try {
			md5(pramap, secret);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		String sign = pramap.get("sign");
		System.out.println("加签:" + sign);
		//验签
		try {
			boolean bFlag = validatemd5(pramap,secret,sign);
			System.out.println("验签结果:" + String.valueOf(bFlag));
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
